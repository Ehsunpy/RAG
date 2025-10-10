# با Azure Form Recognizer می‌توانید جداول را به صورت خودکار استخراج کنید
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# تنظیمات Azure
endpoint = "https://your-endpoint.cognitiveservices.azure.com/"
credential = AzureKeyCredential("your-key")
document_analysis_client = DocumentAnalysisClient(endpoint, credential)

# آنالیز PDF
with open("MBS-guide.pdf", "rb") as f:
    poller = document_analysis_client.begin_analyze_document(
        "prebuilt-layout", document=f
    )
    result = poller.result()

# پردازش جداول
for table in result.tables:
    for cell in table.cells:
        if "item" in cell.content.lower() and cell.content.strip().isdigit():
            # این یک آیتم MBS است
            process_mbs_item(cell.content, table)