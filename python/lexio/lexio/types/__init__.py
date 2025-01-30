# generated by datamodel-codegen:
#   filename:  types.json
#   timestamp: 2025-01-30T08:32:58+00:00

from __future__ import annotations

from typing import Annotated, Any, List, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel


class Model(RootModel[Any]):
    root: Any


class Message(BaseModel):
    """
    Represents a single message in a conversation between a user and an assistant.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    role: Annotated[Literal['assistant', 'user'], Field(title='role')]
    """
    The role of the message sender.
    Can be either "user" for user messages or "assistant" for AI responses.
    """
    content: Annotated[str, Field(title='content')]
    """
    The actual text content of the message.
    """


class Rect(BaseModel):
    """
    The rectangle coordinates of the highlight
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    top: Annotated[float, Field(title='top')]
    """
    Top position of the highlight (relative to the page)
    """
    left: Annotated[float, Field(title='left')]
    """
    Left position of the highlight (relative to the page)
    """
    width: Annotated[float, Field(title='width')]
    """
    Width of the highlight (relative to the page width)
    """
    height: Annotated[float, Field(title='height')]
    """
    Height of the highlight (relative to the page height)
    """


class PDFHighlight(BaseModel):
    """
    Represents a highlight annotation in a PDF document.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    page: Annotated[float, Field(title='page')]
    """
    The page number where the highlight appears. Page numbers are 1-based.
    """
    rect: Annotated[Rect, Field(title='rect')]
    """
    The rectangle coordinates of the highlight
    """


class RetrieveResponse(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    field___toStringTag_23: Annotated[
        str, Field(alias='__@toStringTag@23', title='__@toStringTag@23')
    ]


class GenerateInput(RootModel[List[Message]]):
    root: List[Message]


class AsyncIterableGenerateStreamChunk(RootModel[Any]):
    root: Any


class PromiseString(RootModel[Any]):
    root: Any


class Record(RootModel[Any]):
    root: Any


class Uint8Array(RootModel[Any]):
    root: Any


class BaseSourceContent(BaseModel):
    """
    Base interface for all source content types.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    metadata: Annotated[Optional[Record], Field(title='metadata')] = None
    """
    Optional metadata associated with the content. Can be used to store additional information.
    """


class BaseRetrievalResult(BaseModel):
    """
    Base interface for all retrieval results, providing common properties.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    sourceName: Annotated[Optional[str], Field(title='sourceName')] = None
    """
    Optional name of the source document. If not provided, the source reference will be used.
    """
    relevanceScore: Annotated[
        Optional[float], Field(ge=0.0, le=1.0, title='relevanceScore')
    ] = None
    """
    Optional score indicating relevance to the query. Scores must be in the range [0, 1].
    """
    metadata: Annotated[Optional[Record], Field(title='metadata')] = None
    """
    Optional metadata associated with the result. Can be used to store additional information.
    """
    highlights: Annotated[Optional[List[PDFHighlight]], Field(title='highlights')] = (
        None
    )
    """
    Optional array of PDF highlights. Only used for PDF source references.
    """


class SourceReference(BaseModel):
    """
    Represents a reference to a source document.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    type: Annotated[
        Optional[Literal['html', 'markdown', 'pdf']], Field(title='type')
    ] = None
    """
    The type of the source document. Can be either "pdf", "html", or "markdown".
    """
    sourceReference: Annotated[str, Field(title='sourceReference')]
    """
    Reference identifier for the source. This can be everything from a URL, over a unique identifier to a database key and must be handled by the user in the getDataSource function.
    """
    sourceName: Annotated[Optional[str], Field(title='sourceName')] = None
    """
    Optional name of the source document. If not provided, the source reference will be used.
    """
    relevanceScore: Annotated[
        Optional[float], Field(ge=0.0, le=1.0, title='relevanceScore')
    ] = None
    """
    Optional score indicating relevance to the query. Scores must be in the range [0, 1].
    """
    metadata: Annotated[Optional[Record], Field(title='metadata')] = None
    """
    Optional metadata associated with the result. Can be used to store additional information.
    """
    highlights: Annotated[Optional[List[PDFHighlight]], Field(title='highlights')] = (
        None
    )
    """
    Optional array of PDF highlights. Only used for PDF source references.
    """


class TextContent(BaseModel):
    """
    Represents extracted text content from a source.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    text: Annotated[str, Field(title='text')]
    """
    The content of the RetrievalResult. If you are using the ComponentDisplay component, the text will be displayed with the **MarkdownViewer** component.
    """
    sourceName: Annotated[Optional[str], Field(title='sourceName')] = None
    """
    Optional name of the source document. If not provided, the source reference will be used.
    """
    relevanceScore: Annotated[
        Optional[float], Field(ge=0.0, le=1.0, title='relevanceScore')
    ] = None
    """
    Optional score indicating relevance to the query. Scores must be in the range [0, 1].
    """
    metadata: Annotated[Optional[Record], Field(title='metadata')] = None
    """
    Optional metadata associated with the result. Can be used to store additional information.
    """
    highlights: Annotated[Optional[List[PDFHighlight]], Field(title='highlights')] = (
        None
    )
    """
    Optional array of PDF highlights. Only used for PDF source references.
    """


class MarkdownSourceContent(BaseModel):
    """
    Represents Markdown source content.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    content: Annotated[str, Field(title='content')]
    """
    The Markdown content as a string.
    """
    type: Annotated[Literal['markdown'], Field(title='type')] = 'markdown'
    """
    Must be "markdown". Indicates this is Markdown content.
    """
    metadata: Annotated[Optional[Record], Field(title='metadata')] = None
    """
    Optional metadata associated with the content. Can be used to store additional information.
    """


class HTMLSourceContent(BaseModel):
    """
    Represents HTML source content.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    content: Annotated[str, Field(title='content')]
    """
    The HTML content as a string.
    """
    type: Annotated[Literal['html'], Field(title='type')] = 'html'
    """
    Must be "html". Indicates this is HTML content.
    """
    metadata: Annotated[Optional[Record], Field(title='metadata')] = None
    """
    Optional metadata associated with the content. Can be used to store additional information.
    """


class PDFSourceContent(BaseModel):
    """
    Represents PDF source content.
    """

    model_config = ConfigDict(
        extra='forbid',
    )
    content: Annotated[Uint8Array, Field(title='content')]
    """
    The binary PDF content.
    """
    type: Annotated[Literal['pdf'], Field(title='type')] = 'pdf'
    """
    Must be "pdf". Indicates this is PDF content.
    """
    highlights: Annotated[Optional[List[PDFHighlight]], Field(title='highlights')] = (
        None
    )
    """
    Optional array of highlights in the PDF.
    """
    metadata: Annotated[Optional[Record], Field(title='metadata')] = None
    """
    Optional metadata associated with the content. Can be used to store additional information.
    """


class SourceContent(
    RootModel[Union[MarkdownSourceContent, HTMLSourceContent, PDFSourceContent]]
):
    root: Annotated[
        Union[MarkdownSourceContent, HTMLSourceContent, PDFSourceContent],
        Field(title='SourceContent'),
    ]


class GenerateResponse(
    RootModel[Union[PromiseString, AsyncIterableGenerateStreamChunk]]
):
    root: Annotated[
        Union[PromiseString, AsyncIterableGenerateStreamChunk],
        Field(title='GenerateResponse'),
    ]


class RetrievalResult(RootModel[Union[SourceReference, TextContent]]):
    root: Annotated[Union[SourceReference, TextContent], Field(title='RetrievalResult')]
