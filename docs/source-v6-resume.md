# 다음 작업의 시작점

최신 원본은 `production/source-v6-approved-pages.json`, 컷별 정보는 `assets/seq01/source-v6/panels.json`, 음성 시간축은 `assets/seq01/source-v6/timing.json`이다. HTML 생성기는 `production/build-source-v6.py`, 재생 코드는 `assets/seq01/source-v6-reader.js`다.

원본 PNG 28개는 수정된 최종 원화다. 초기 생성 프롬프트 파일은 첫 생성 기준이며, 이후 검수 수정은 `docs/source-v6-review.md`를 함께 읽는다. PNG를 바꾸면 생성기를 다시 실행해 WebP와 컷 경계를 갱신한다.

마지막 4컷은 이전 작업 기록이 잘려 복원한 부분이다. 다음 시퀀스 고해성사와 의뢰인·배후·보수·미래 손상의 설정을 임의로 추가하지 않는다.

한 번에 원화 28개를 모델 입력으로 넣지 않는다. 중단 오류는 입력 이미지 합산 크기 초과였다. 필요한 인물·장소 참고와 대상 컷만 소수로 읽고 수정한다.

새 배포에서 이미 공개한 v6 자산을 바꿀 때에는 v7처럼 새 버전 경로나 캐시를 구분하는 값을 사용한다. 자산의 장기 캐시 때문에 같은 주소를 덮어쓰면 이전 그림이나 음성이 남을 수 있다. 미리보기 서버는 MP3·MP4의 Range 응답을 지원해야 중간 컷의 음성·영상 탐색을 검수할 수 있다.
