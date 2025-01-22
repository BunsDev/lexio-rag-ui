# generated by datamodel-codegen:
#   filename:  openapi-schema.json
#   timestamp: 2025-01-22T20:32:35+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Extra, Field


class Model(BaseModel):
    __root__: Any


class Message(BaseModel):
    class Config:
        extra = Extra.forbid

    role: str = Field(..., title='role')
    content: str = Field(..., title='content')


class Type(Enum):
    html = 'html'
    markdown = 'markdown'
    pdf = 'pdf'


class Rect(BaseModel):
    class Config:
        extra = Extra.forbid

    top: int = Field(..., title='top')
    left: int = Field(..., title='left')
    width: int = Field(..., title='width')
    height: int = Field(..., title='height')


class PDFHighlight(BaseModel):
    class Config:
        extra = Extra.forbid

    page: int = Field(..., title='page')
    rect: Rect = Field(..., title='rect')
    comment: Optional[str] = Field(None, title='comment')


class RetrieveResponse(BaseModel):
    class Config:
        extra = Extra.forbid

    field___toStringTag_23: str = Field(
        ..., alias='__@toStringTag@23', title='__@toStringTag@23'
    )


class GenerateInput(BaseModel):
    __root__: List[Message]


class ArrayBufferLike(BaseModel):
    __root__: Any


class AsyncIterableGenerateStreamChunk(BaseModel):
    __root__: Any


class PromiseString(BaseModel):
    __root__: Any


class RecordStringAny(BaseModel):
    __root__: Any


class BaseSourceContent(BaseModel):
    class Config:
        extra = Extra.forbid

    metadata: Optional[RecordStringAny] = Field(None, title='metadata')


class BaseRetrievalResult(BaseModel):
    class Config:
        extra = Extra.forbid

    sourceName: Optional[str] = Field(None, title='sourceName')
    relevanceScore: Optional[int] = Field(None, title='relevanceScore')
    metadata: Optional[RecordStringAny] = Field(None, title='metadata')
    highlights: Optional[List[PDFHighlight]] = Field(None, title='highlights')


class SourceReference(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[Type] = Field(None, title='type')
    sourceReference: str = Field(..., title='sourceReference')
    sourceName: Optional[str] = Field(None, title='sourceName')
    relevanceScore: Optional[int] = Field(None, title='relevanceScore')
    metadata: Optional[RecordStringAny] = Field(None, title='metadata')
    highlights: Optional[List[PDFHighlight]] = Field(None, title='highlights')


class TextContent(BaseModel):
    class Config:
        extra = Extra.forbid

    text: str = Field(..., title='text')
    sourceName: Optional[str] = Field(None, title='sourceName')
    relevanceScore: Optional[int] = Field(None, title='relevanceScore')
    metadata: Optional[RecordStringAny] = Field(None, title='metadata')
    highlights: Optional[List[PDFHighlight]] = Field(None, title='highlights')


class MarkdownSourceContent(BaseModel):
    class Config:
        extra = Extra.forbid

    content: str = Field(..., title='content')
    type: str = Field('markdown', const=True, title='type')
    metadata: Optional[RecordStringAny] = Field(None, title='metadata')


class HTMLSourceContent(BaseModel):
    class Config:
        extra = Extra.forbid

    content: str = Field(..., title='content')
    type: str = Field('html', const=True, title='type')
    metadata: Optional[RecordStringAny] = Field(None, title='metadata')


class Content(BaseModel):
    class Config:
        extra = Extra.forbid

    BYTES_PER_ELEMENT: int = Field(..., title='BYTES_PER_ELEMENT')
    buffer: ArrayBufferLike = Field(..., title='buffer')
    byteLength: int = Field(..., title='byteLength')
    byteOffset: int = Field(..., title='byteOffset')
    length: int = Field(..., title='length')
    field___toStringTag_23: str = Field(
        'Uint8Array', alias='__@toStringTag@23', const=True, title='__@toStringTag@23'
    )


class PDFSourceContent(BaseModel):
    class Config:
        extra = Extra.forbid

    content: Content = Field(..., title='content')
    type: str = Field('pdf', const=True, title='type')
    highlights: Optional[List[PDFHighlight]] = Field(None, title='highlights')
    metadata: Optional[RecordStringAny] = Field(None, title='metadata')


class SourceContent(BaseModel):
    __root__: Union[MarkdownSourceContent, HTMLSourceContent, PDFSourceContent]


class GenerateResponse(BaseModel):
    __root__: Union[PromiseString, AsyncIterableGenerateStreamChunk]


class RetrievalResult(BaseModel):
    __root__: Union[SourceReference, TextContent]
