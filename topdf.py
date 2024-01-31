import img2pdf
from PIL import Image
import os
from PyPDF2 import PdfReader, PdfWriter
#from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet

path = os.getcwd()
in_path = os.path.join(path, "threshed")
pdfpath = os.path.join(path, "pdfs")
final_path = os.path.join(path, "Final//result.pdf")



def main():
    make_pdfs()
    compress_pdfs_and_merge()
    #lossy_compress()

def make_pdfs():
    for image_path in os.listdir(in_path):
        full_path = os.path.join(in_path, image_path)
        image = Image.open(full_path)
        pdf_bytes = img2pdf.convert(image.filename)

        

        pdf_full_path = os.path.join(pdfpath, image_path[:-4] + ".pdf")
        file = open(pdf_full_path, "wb")
        file.write(pdf_bytes)
        image.close()
        file.close()

def compress_pdfs_and_merge():
    writer = PdfWriter()
    #presize = 0
    for image_path in os.listdir(pdfpath):
        full_path = os.path.join(pdfpath, image_path)
        #presize += os.stat(full_path).st_size
        reader = PdfReader(full_path)
        
        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)
        writer.add_metadata(reader.metadata)
    with open(final_path, "wb") as f:
        writer.write(f)
    #postsize = os.stat(finalpath).st_size
    #print("Filesize before compression: " + sizeof_fmt(presize) + "\n" + "Filesize after compression: " + sizeof_fmt(postsize))


#currently needs a license to use, i should use ilovepdf instead
#def lossy_compress():
#    presize = os.stat(final_path).st_size
#    PDFNet.Initialize()
#    doc = PDFDoc(final_path)
#    doc.InitSecurityHandler()
#    Optimizer.Optimize(doc)
#    doc.Save(final_path, SDFDoc.e_linearized)
#    doc.Close()
#    postsize = os.stat(final_path).st_size
#    print("Filesize before compression: " + sizeof_fmt(presize) + "\n" + "Filesize after compression: " + sizeof_fmt(postsize))




#get human-readable file size, attr. Fred Cirera
def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"




if __name__ == "__main__":
    main()