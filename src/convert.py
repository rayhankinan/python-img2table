from io import BytesIO
from typing import Iterator, List, Tuple

from img2table.document import PDF
from img2table.ocr import VisionOCR
from img2table.tables.objects.extraction import ExtractedTable
import pandas as pd

from config import config

def convert_tables_into_dataframe(tables: List[ExtractedTable]) -> Iterator[pd.DataFrame]:
    for table in tables:
        yield table.df

def convert_pdf_to_dataframe(stream: BytesIO) -> Iterator[Tuple[int, Iterator[pd.DataFrame]]]:
    doc = PDF(src=stream, pdf_text_extraction=False)
    ocr = VisionOCR(api_key=config["GCP_VISION_API_KEY"])
    extracted_tables = doc.extract_tables(ocr=ocr)

    for page, tables in extracted_tables.items():
        yield page, convert_tables_into_dataframe(tables)