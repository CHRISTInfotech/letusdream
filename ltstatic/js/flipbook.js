document.addEventListener('DOMContentLoaded', () => {
    const flipbook = document.getElementById('flipbook');
    const pdfUrl = flipbook.getAttribute('data-url');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    const resetButton = document.getElementById('reset');

    if (!pdfUrl) {
        console.error("No PDF URL provided for the flipbook.");
        return;
    }

    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.worker.min.js';

    const loadPDF = async () => {
        try {
            const pdf = await pdfjsLib.getDocument(pdfUrl).promise;
            const pageCount = pdf.numPages;

            let currentPage = 1;

            const renderPage = async (pageNumber) => {
                if (pageNumber < 1 || pageNumber > pageCount) return null;
            
                const pageDiv = document.createElement('div');
                pageDiv.classList.add('page');
            
                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d');
            
                const pdfPage = await pdf.getPage(pageNumber);
            
                // Get flipbook dimensions
                const flipbookWidth = flipbook.clientWidth ; // Half width for each page
                const flipbookHeight = flipbook.clientHeight;
            
                // Scale the PDF page to fit within the flipbook
                const viewport = pdfPage.getViewport({ scale: 1 });
                const scale = Math.min(
                    flipbookWidth / viewport.width,
                    flipbookHeight / viewport.height
                );
            
                const scaledViewport = pdfPage.getViewport({ scale });
            
                // Set canvas size to match the scaled dimensions
                canvas.width = scaledViewport.width;
                canvas.height = scaledViewport.height;
            
                // Render the PDF page onto the canvas
                await pdfPage.render({
                    canvasContext: context,
                    viewport: scaledViewport,
                }).promise;
            
                pageDiv.appendChild(canvas);
                return pageDiv;
            };
            

            const renderPages = async () => {
                flipbook.innerHTML = ''; // Clear existing pages

                const leftPage = await renderPage(currentPage);
                if (leftPage) {
                    leftPage.style.transform = 'rotateY(0deg)';
                    flipbook.appendChild(leftPage);
                }

                const rightPage = await renderPage(currentPage + 1);
                if (rightPage) {
                    rightPage.style.transform = 'rotateY(-180deg)';
                    flipbook.appendChild(rightPage);
                }

                prevButton.disabled = currentPage <= 1;
                nextButton.disabled = currentPage + 1 >= pageCount;
            };

            const flipPage = (direction) => {
                if (direction === 'next' && currentPage + 2 <= pageCount) {
                    currentPage += 2;
                } else if (direction === 'prev' && currentPage - 2 >= 1) {
                    currentPage -= 2;
                } else if (direction === 'reset') {
                    currentPage = 1;
                }
                renderPages();
            };

            prevButton.addEventListener('click', () => flipPage('prev'));
            nextButton.addEventListener('click', () => flipPage('next'));
            resetButton.addEventListener('click', () => flipPage('reset'));

            await renderPages();
        } catch (error) {
            console.error('Error loading PDF:', error);
        }
    };

    loadPDF();
});
