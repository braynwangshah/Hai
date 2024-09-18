from _typeshed import Incomplete
from typing import IO, Literal

from reportlab.lib.colors import Color, _ConvertibleToColor
from reportlab.pdfgen.textobject import PDFTextObject, _PDFColorSetter

class ShowBoundaryValue:
    color: _ConvertibleToColor | None
    width: float
    dashArray: Incomplete
    def __init__(
        self,
        color: _ConvertibleToColor | None = (0, 0, 0),
        width: float = 0.1,
        dashArray: list[float] | tuple[float, ...] | None = None,
    ) -> None: ...
    def __bool__(self) -> bool: ...

class Canvas(_PDFColorSetter):
    bottomup: int
    imageCaching: Incomplete
    state_stack: Incomplete
    def __init__(
        self,
        filename: str | IO[bytes],
        pagesize: tuple[float, float] | None = None,
        bottomup: int = 1,
        pageCompression: Incomplete | None = None,
        invariant: Incomplete | None = None,
        verbosity: int = 0,
        encrypt: Incomplete | None = None,
        cropMarks: Incomplete | None = None,
        pdfVersion: Incomplete | None = None,
        enforceColorSpace: Incomplete | None = None,
        initialFontName: float | None = None,
        initialFontSize: float | None = None,
        initialLeading: float | None = None,
        cropBox: Incomplete | None = None,
        artBox: Incomplete | None = None,
        trimBox: Incomplete | None = None,
        bleedBox: Incomplete | None = None,
        lang: Incomplete | None = None,
    ) -> None: ...
    def setEncrypt(self, encrypt) -> None: ...
    def init_graphics_state(self) -> None: ...
    def push_state_stack(self) -> None: ...
    def pop_state_stack(self) -> None: ...
    STATE_ATTRIBUTES: Incomplete
    STATE_RANGE: Incomplete
    def setAuthor(self, author: str | None) -> None: ...
    def setDateFormatter(self, dateFormatter) -> None: ...
    def addOutlineEntry(self, title, key, level: int = 0, closed: Incomplete | None = None) -> None: ...
    def setOutlineNames0(self, *nametree) -> None: ...
    def setTitle(self, title: str | None) -> None: ...
    def setSubject(self, subject: str | None) -> None: ...
    def setCreator(self, creator: str | None) -> None: ...
    def setProducer(self, producer: str | None) -> None: ...
    def setKeywords(self, keywords: str | None) -> None: ...
    def pageHasData(self): ...
    def showOutline(self) -> None: ...
    def showFullScreen0(self) -> None: ...
    def setBlendMode(self, v) -> None: ...
    def showPage(self) -> None: ...
    def setPageCallBack(self, func) -> None: ...
    def bookmarkPage(
        self,
        key,
        fit: str = "Fit",
        left: Incomplete | None = None,
        top: Incomplete | None = None,
        bottom: Incomplete | None = None,
        right: Incomplete | None = None,
        zoom: Incomplete | None = None,
    ): ...
    def bookmarkHorizontalAbsolute(self, key, top, left: int = 0, fit: str = "XYZ", **kw): ...
    def bookmarkHorizontal(self, key, relativeX, relativeY, **kw) -> None: ...
    def doForm(self, name) -> None: ...
    def hasForm(self, name): ...
    def drawInlineImage(
        self,
        image,
        x: float,
        y: float,
        width: float | None = None,
        height: float | None = None,
        preserveAspectRatio: bool = False,
        anchor: str = "c",
        anchorAtXY: bool = False,
        showBoundary: bool = False,
        extraReturn: Incomplete | None = None,
    ): ...
    def drawImage(
        self,
        image,
        x: float,
        y: float,
        width: float | None = None,
        height: float | None = None,
        mask: Incomplete | None = None,
        preserveAspectRatio: bool = False,
        anchor: str = "c",
        anchorAtXY: bool = False,
        showBoundary: bool = False,
        extraReturn: Incomplete | None = None,
    ): ...
    def beginForm(
        self, name, lowerx: int = 0, lowery: int = 0, upperx: Incomplete | None = None, uppery: Incomplete | None = None
    ) -> None: ...
    def endForm(self, **extra_attributes) -> None: ...
    def addPostScriptCommand(self, command, position: int = 1) -> None: ...
    def freeTextAnnotation(
        self,
        contents,
        DA,
        Rect: Incomplete | None = None,
        addtopage: int = 1,
        name: Incomplete | None = None,
        relative: int = 0,
        **kw,
    ) -> None: ...
    def textAnnotation(
        self,
        contents,
        Rect: Incomplete | None = None,
        addtopage: int = 1,
        name: Incomplete | None = None,
        relative: int = 0,
        **kw,
    ) -> None: ...
    textAnnotation0 = textAnnotation
    def highlightAnnotation(
        self,
        contents,
        Rect,
        QuadPoints: Incomplete | None = None,
        Color=[0.83, 0.89, 0.95],
        addtopage: int = 1,
        name: Incomplete | None = None,
        relative: int = 0,
        **kw,
    ) -> None: ...
    def inkAnnotation(
        self,
        contents,
        InkList: Incomplete | None = None,
        Rect: Incomplete | None = None,
        addtopage: int = 1,
        name: Incomplete | None = None,
        relative: int = 0,
        **kw,
    ) -> None: ...
    inkAnnotation0 = inkAnnotation
    def linkAbsolute(
        self,
        contents,
        destinationname,
        Rect: Incomplete | None = None,
        addtopage: int = 1,
        name: Incomplete | None = None,
        thickness: int = 0,
        color: Color | None = None,
        dashArray: Incomplete | None = None,
        **kw,
    ): ...
    def linkRect(
        self,
        contents,
        destinationname,
        Rect: Incomplete | None = None,
        addtopage: int = 1,
        name: Incomplete | None = None,
        relative: int = 1,
        thickness: int = 0,
        color: Color | None = None,
        dashArray: Incomplete | None = None,
        **kw,
    ): ...
    def linkURL(
        self,
        url,
        rect,
        relative: int = 0,
        thickness: int = 0,
        color: Color | None = None,
        dashArray: Incomplete | None = None,
        kind: str = "URI",
        **kw,
    ) -> None: ...
    def getPageNumber(self): ...
    def save(self) -> None: ...
    def getpdfdata(self): ...
    def setPageSize(self, size: tuple[float, float]) -> None: ...
    def setCropBox(self, size, name: str = "crop") -> None: ...
    def setTrimBox(self, size) -> None: ...
    def setArtBox(self, size) -> None: ...
    def setBleedBox(self, size) -> None: ...
    # NOTE: Only accepts right angles
    def setPageRotation(self, rot: float) -> None: ...
    def addLiteral(self, s: object, escaped: int = 1) -> None: ...
    def resetTransforms(self) -> None: ...
    def transform(self, a: float, b: float, c: float, d: float, e: float, f: float) -> None: ...
    def absolutePosition(self, x: float, y: float) -> tuple[float, float]: ...
    def translate(self, dx: float, dy: float) -> None: ...
    def scale(self, x: float, y: float) -> None: ...
    def rotate(self, theta: float) -> None: ...
    def skew(self, alpha: float, beta: float) -> None: ...
    def saveState(self) -> None: ...
    def restoreState(self) -> None: ...
    def line(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    def lines(self, linelist) -> None: ...
    def cross(
        self,
        x: float,
        y: float,
        size: float = 5,
        gap: float = 1,
        text: Incomplete | None = None,
        strokeColor: Incomplete | None = None,
        strokeWidth: float | None = None,
        fontSize: float = 3,
    ) -> None: ...
    def grid(self, xlist, ylist) -> None: ...
    def bezier(self, x1, y1, x2, y2, x3, y3, x4, y4) -> None: ...
    def arc(self, x1, y1, x2, y2, startAng: int = 0, extent: int = 90) -> None: ...
    def rect(self, x, y, width, height, stroke: int = 1, fill: int = 0) -> None: ...
    def ellipse(self, x1, y1, x2, y2, stroke: int = 1, fill: int = 0) -> None: ...
    def wedge(self, x1, y1, x2, y2, startAng, extent, stroke: int = 1, fill: int = 0) -> None: ...
    def circle(self, x_cen, y_cen, r, stroke: int = 1, fill: int = 0) -> None: ...
    def roundRect(self, x, y, width, height, radius, stroke: int = 1, fill: int = 0) -> None: ...
    def shade(self, shading) -> None: ...
    def linearGradient(self, x0, y0, x1, y1, colors, positions: Incomplete | None = None, extend: bool = True) -> None: ...
    def radialGradient(self, x, y, radius, colors, positions: Incomplete | None = None, extend: bool = True) -> None: ...
    def drawString(
        self,
        x: float,
        y: float,
        text: str,
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
    ) -> None: ...
    def drawRightString(
        self,
        x: float,
        y: float,
        text: str,
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
    ) -> None: ...
    def drawCentredString(
        self,
        x: float,
        y: float,
        text: str,
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
    ) -> None: ...
    def drawAlignedString(
        self,
        x: float,
        y: float,
        text: str,
        pivotChar: str = ".",
        mode: Literal[0, 1, 2, 3, 4, 5, 6, 7] | None = None,
        charSpace: float = 0,
        direction: Literal["LTR", "RTL"] | None = None,
        wordSpace: float | None = None,
    ) -> None: ...
    def getAvailableFonts(self): ...
    def listLoadedFonts0(self): ...
    def setFont(self, psfontname: str, size: float, leading: float | None = None) -> None: ...
    def setFontSize(self, size: float | None = None, leading: float | None = None) -> None: ...
    def stringWidth(self, text: str, fontName: str | None = None, fontSize: float | None = None) -> float: ...
    def setLineWidth(self, width: float) -> None: ...
    def setLineCap(self, mode) -> None: ...
    def setLineJoin(self, mode) -> None: ...
    def setMiterLimit(self, limit) -> None: ...
    def setDash(self, array: list[float] | tuple[float, ...] | float = [], phase: float = 0) -> None: ...
    def beginPath(self): ...
    def drawPath(self, aPath, stroke: int = 1, fill: int = 0, fillMode: Incomplete | None = None) -> None: ...
    def clipPath(self, aPath, stroke: int = 1, fill: int = 0, fillMode: Incomplete | None = None) -> None: ...
    def beginText(self, x: float = 0, y: float = 0, direction: Literal["LTR", "RTL"] | None = None) -> PDFTextObject: ...
    def drawText(self, aTextObject: PDFTextObject) -> None: ...
    def setPageCompression(self, pageCompression: int = 1) -> None: ...
    def setPageDuration(self, duration: Incomplete | None = None) -> None: ...
    def setPageTransition(
        self, effectname: str | None = None, duration: float = 1, direction: float = 0, dimension: str = "H", motion: str = "I"
    ) -> None: ...
    def getCurrentPageContent(self): ...
    def setViewerPreference(self, pref, value) -> None: ...
    def getViewerPreference(self, pref): ...
    def delViewerPreference(self, pref) -> None: ...
    def setCatalogEntry(self, key, value) -> None: ...
    def getCatalogEntry(self, key): ...
    def delCatalogEntry(self, key) -> None: ...
    def addPageLabel(
        self, pageNum, style: Incomplete | None = None, start: Incomplete | None = None, prefix: Incomplete | None = None
    ) -> None: ...
    @property
    def acroForm(self): ...
    def drawBoundary(self, sb, x1: float, y1: float, width: float, height: float) -> None: ...
