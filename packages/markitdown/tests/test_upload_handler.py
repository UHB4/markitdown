# tests/test_upload_handler.py
import os
import pytest
from markitdown import MarkItDown, StreamInfo

# 더미 업로드 콜백 함수
def dummy_upload_handler(image_blob, meta):
    return f"http://dummy.com/{meta['filename']}"

TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), "test_files")

@pytest.mark.parametrize("filename", ["test.pptx"])
def test_convert_with_upload_handler(filename):
    """
    PPTX 파일 변환 시, upload_handler를 전달하면
    반환된 마크다운에 dummy URL이 포함되는지 확인합니다.
    """
    markitdown = MarkItDown()

    file_path = os.path.join(TEST_FILES_DIR, filename)
    
    stream_info = StreamInfo(
        extension=".pptx", 
        mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        charset=None
    )

    with open(file_path, "rb") as stream:
        result = markitdown.convert(
            stream,
            stream_info=stream_info,
            upload_handler=dummy_upload_handler,  # 업로드 콜백 함수 전달
            url=None  # 기존의 url 매개변수와는 별도로 콜백 기능 사용
        )
    
    # dummy_upload_handler가 반환하는 URL이 Markdown에 포함되어야 함
    expected_substring = "http://dummy.com/"
    assert expected_substring in result.markdown, "upload_handler에서 반환한 URL이 포함되어야 합니다."
