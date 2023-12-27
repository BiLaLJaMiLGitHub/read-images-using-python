from utils import imageToString

if __name__ == '__main__':
    ir = imageToString.ImageReader(imageToString.OS.Mac)
    text = ir.extract_text('question.png', lang='en' )
    print("Document Text: ", text)
