import os
import http.server
import socketserver

PORT = 8000
BASE_DIR = os.path.dirname(__file__)
DIRECTORY = os.path.join(BASE_DIR, "uploaded_images")

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        """
        URL 경로가 /uploaded_images/로 시작하면, 해당 경로를 DIRECTORY로 매핑합니다.
        예를 들어, 
          http://localhost:8000/uploaded_images/team.jpg
        요청 시, DIRECTORY/team.jpg 파일을 반환합니다.
        """
        if path.startswith("/uploaded_images/"):
            # /uploaded_images/ 를 제거하고 나머지 경로를 DIRECTORY에 붙임
            path = path[len("/uploaded_images/"):]
        else:
            # 그 외의 요청은 빈 문자열 반환(혹은 기본 동작)
            path = ""
        return os.path.join(DIRECTORY, path)

# TCPServer를 사용하여 지정한 PORT에서 CustomHandler로 HTTP 서버 실행
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"서버가 http://localhost:{PORT}/uploaded_images/ 에서 정적 파일을 서빙합니다.")
    httpd.serve_forever()
