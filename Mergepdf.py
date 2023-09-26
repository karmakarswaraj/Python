import PyPDF2
import os

directory = r"C:\Users\Swaraj\Desktop\COLLEGE\UDEMY CIR\ALL"

# List PDF files in the directory
pdf_files = [os.path.join(directory, filename) #Ensure it is platform independent
                for filename in os.listdir(directory) 
                    if filename.endswith(".pdf")]

# Create a PDF merger object
pdf_merger = PyPDF2.PdfFileMerger() #use merge property available

# Append PDF files to the merger
for pdf_file in pdf_files:
    pdf_merger.append(pdf_file)

# Output merged PDF to a file
output_pdf = os.path.join(directory, "merged.pdf")
pdf_merger.write(output_pdf)

# Close the merger object
pdf_merger.close()