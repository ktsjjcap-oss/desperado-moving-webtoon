export default {
 async fetch(request, env) {
  if (!['/assets/seq01/master.mp4','/assets/seq01/story-v2.mp4'].includes(new URL(request.url).pathname) || !['GET','HEAD'].includes(request.method)) return env.ASSETS.fetch(request);
  const range = request.headers.get('range');
  const upstreamHeaders = new Headers(request.headers);
  upstreamHeaders.delete('range');
  const response = await env.ASSETS.fetch(new Request(request.url, {method:'GET',headers:upstreamHeaders}));
  if (response.status !== 200) return response;
  const headers = new Headers(response.headers);
  headers.set('Accept-Ranges','bytes');
  if (!range || (request.headers.has('if-range') && request.headers.get('if-range') !== headers.get('etag'))) {
   if (request.method === 'HEAD') { await response.body?.cancel(); return new Response(null,{status:200,headers}); }
   return new Response(response.body,{status:200,headers});
  }
  const bytes = await response.arrayBuffer();
  const total = bytes.byteLength;
  const match = /^bytes=(\d*)-(\d*)$/.exec(range);
  let start, end;
  if (match && (match[1] || match[2])) {
   start = match[1] ? Number(match[1]) : Math.max(0,total-Number(match[2]));
   end = match[1] ? (match[2] ? Math.min(Number(match[2]),total-1) : total-1) : total-1;
  }
  if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start > end || start >= total || (match && !match[1] && Number(match[2]) === 0)) {
   headers.set('Content-Range',`bytes */${total}`); headers.set('Content-Length','0');
   return new Response(null,{status:416,headers});
  }
  headers.set('Content-Range',`bytes ${start}-${end}/${total}`);
  headers.set('Content-Length',String(end-start+1));
  return new Response(request.method === 'HEAD' ? null : bytes.slice(start,end+1),{status:206,headers});
 }
};
