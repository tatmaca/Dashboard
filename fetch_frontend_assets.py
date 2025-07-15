import os
import urllib.request

base_dir = "src/main/resources/public/vendors"

assets = {
    # CSS
    "bootstrap/css/bootstrap.min.css": "https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css",
    "datatables.net-bs/css/dataTables.bootstrap.min.css": "https://cdn.jsdelivr.net/npm/datatables.net-bs@1.10.25/css/dataTables.bootstrap.min.css",
    "datatables.net-buttons-bs/css/buttons.bootstrap.min.css": "https://cdn.jsdelivr.net/npm/datatables.net-buttons-bs@1.7.1/css/buttons.bootstrap.min.css",
    "datatables.net-scroller-bs/css/scroller.bootstrap.min.css": "https://cdn.jsdelivr.net/npm/datatables.net-scroller-bs@1.4.0/css/scroller.bootstrap.min.css",
    "datatables.net-fixedheader-bs/css/fixedHeader.bootstrap.min.css": "https://cdn.jsdelivr.net/npm/datatables.net-fixedheader-bs@3.1.9/css/fixedHeader.bootstrap.min.css",
    "datatables.net-responsive-bs/css/responsive.bootstrap.min.css": "https://cdn.jsdelivr.net/npm/datatables.net-responsive-bs@2.2.9/css/responsive.bootstrap.min.css",
    # JS
    "jquery/jquery.min.js": "https://cdn.jsdelivr.net/npm/jquery@3.6.4/dist/jquery.min.js",
    "bootstrap/js/bootstrap.min.js": "https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/js/bootstrap.min.js",
    "fastclick/fastclick.js": "https://cdn.jsdelivr.net/npm/fastclick@1.0.6/lib/fastclick.js",
    "html2canvas/html2canvas.min.js": "https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js",
    "html2canvas/html2canvas.svg.min.js": "https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.svg.min.js",
    "pdfmake/pdfmake.min.js": "https://cdn.jsdelivr.net/npm/pdfmake@0.1.72/build/pdfmake.min.js",
    "pdfmake/vfs_fonts.js": "https://cdn.jsdelivr.net/npm/pdfmake@0.1.72/build/vfs_fonts.js",
    "datatables.net/js/jquery.dataTables.min.js": "https://cdn.jsdelivr.net/npm/datatables.net@1.10.25/js/jquery.dataTables.min.js",
    "datatables.net-bs/js/dataTables.bootstrap.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-bs@1.10.25/js/dataTables.bootstrap.min.js",
    "datatables.net-buttons/js/dataTables.buttons.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-buttons@1.7.1/js/dataTables.buttons.min.js",
    "datatables.net-buttons-bs/js/buttons.bootstrap.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-buttons-bs@1.7.1/js/buttons.bootstrap.min.js",
    "datatables.net-buttons/js/buttons.html5.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-buttons@1.7.1/js/buttons.html5.min.js",
    "datatables.net-buttons/js/buttons.print.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-buttons@1.7.1/js/buttons.print.min.js",
    "datatables.net-buttons/js/buttons.flash.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-buttons@1.7.1/js/buttons.flash.min.js",
    "datatables.net-keytable/js/dataTables.keyTable.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-keytable@2.6.2/js/dataTables.keyTable.min.js",
    "datatables.net-fixedheader/js/dataTables.fixedHeader.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-fixedheader@3.1.9/js/dataTables.fixedHeader.min.js",
    "datatables.net-responsive/js/dataTables.responsive.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-responsive@2.2.9/js/dataTables.responsive.min.js",
    "datatables.net-responsive-bs/js/responsive.bootstrap.js": "https://cdn.jsdelivr.net/npm/datatables.net-responsive-bs@2.2.9/js/responsive.bootstrap.js",
    "datatables.net-scroller/js/dataTables.scroller.min.js": "https://cdn.jsdelivr.net/npm/datatables.net-scroller@1.4.0/js/dataTables.scroller.min.js",
    "jszip/jszip.min.js": "https://cdn.jsdelivr.net/npm/jszip@3.10.1/dist/jszip.min.js",
}

for relative_path, url in assets.items():
    local_path = os.path.join(base_dir, relative_path)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    print(f"Downloading {url} to {local_path}...")
    try:
        urllib.request.urlretrieve(url, local_path)
    except Exception as e:
        print(f"Failed to download {url}: {e}")
