import os
from markitdown import MarkItDown, StreamInfo

def local_upload_handler(image_blob, meta):
    """
    이미지 데이터를 로컬 폴더 'uploaded_images' 에 저장한 후,
    해당 파일이 정적 서버에서 제공된다고 가정하여 URL을 생성합니다.
    """
    
    current_dir = os.path.dirname(__file__)
    output_dir = os.path.join(current_dir, "uploaded_images")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 이미지 파일 저장 (meta에 저장된 파일명을 사용)
    output_file = os.path.join(output_dir, meta["filename"])
    with open(output_file, "wb") as f:
        f.write(image_blob)

    
    url = f"http://localhost:8000/uploaded_images/{meta['filename']}"
    return url


TEST_FILE_DIR = os.path.join(os.path.dirname(__file__), "test_files")
test_filename = "sample2.pptx" 
test_file_path = os.path.join(TEST_FILE_DIR, test_filename)

markitdown = MarkItDown()

stream_info = StreamInfo(
    extension=".pptx",
    mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    charset=None
)

with open(test_file_path, "rb") as stream:
    result = markitdown.convert(
        stream,
        stream_info=stream_info,
        upload_handler=local_upload_handler,
        url=None
    )

print(result.markdown)
