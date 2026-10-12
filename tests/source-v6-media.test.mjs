import assert from 'node:assert/strict';
import worker from '../worker.mjs';
const bytes=new Uint8Array([0,1,2,3,4,5,6,7,8,9]);
const env={ASSETS:{fetch:async()=>new Response(bytes,{headers:{'content-type':'audio/mpeg','content-length':'10',etag:'test'}})}};
for(const path of ['/assets/seq01/source-v6/dialogue.mp3','/assets/seq01/source-v6/city.mp4','/assets/seq01/source-v6/audio/music.mp3']){
 let r=await worker.fetch(new Request('https://example.com'+path,{headers:{range:'bytes=2-5'}}),env);assert.equal(r.status,206);assert.equal(r.headers.get('content-range'),'bytes 2-5/10');assert.deepEqual([...new Uint8Array(await r.arrayBuffer())],[2,3,4,5]);
 r=await worker.fetch(new Request('https://example.com'+path,{method:'HEAD',headers:{range:'bytes=-3'}}),env);assert.equal(r.status,206);assert.equal(r.headers.get('content-length'),'3');assert.equal((await r.arrayBuffer()).byteLength,0);
 r=await worker.fetch(new Request('https://example.com'+path,{headers:{range:'bytes=15-20'}}),env);assert.equal(r.status,416);
}
console.log('Media seek: 9 range/head/error checks passed');
