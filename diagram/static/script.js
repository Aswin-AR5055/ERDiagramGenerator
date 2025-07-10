window.downloadSVG = function() {
    // Mermaid puts the SVG inside the <pre> with class="mermaid"
    const svgElement = document.querySelector("#mermaidDiagram svg");

    if (!svgElement) {
        alert("Diagram not rendered yet!");
        return;
    }

    // Serialize SVG
    const serializer = new XMLSerializer();
    const svgString = serializer.serializeToString(svgElement);

    // Create a Blob
    const blob = new Blob([svgString], { type: "image/svg+xml;charset=utf-8" });

    // Create a download link
    const url = URL.createObjectURL(blob);
    const downloadLink = document.createElement("a");
    downloadLink.href = url;
    downloadLink.download = "er_diagram.svg";

    // Trigger download
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
};
