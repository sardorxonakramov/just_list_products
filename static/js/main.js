/* ==== DETAIL SAHIFA FUNKSIYALARI ==== */
let images = [];
let currentIndex = 0;

// Asosiy rasmni almashtirish
function changeImage(src, index) {
    const mainImage = document.getElementById("mainImage");
    if (mainImage) {
        mainImage.src = src;
        currentIndex = index;
    }
}

// Modalni ochish
function openModal(index) {
    currentIndex = index;
    const modal = document.getElementById("imageModal");
    const modalImage = document.getElementById("modalImage");

    if (modal && modalImage) {
        modal.style.display = "block";
        modalImage.src = images[currentIndex];
    }
}

// Modalni yopish
function closeModal() {
    const modal = document.getElementById("imageModal");
    if (modal) {
        modal.style.display = "none";
    }
}

// Modal ichida oldinga/ortga yurish
function changeModal(step) {
    if (images.length > 0) {
        currentIndex = (currentIndex + step + images.length) % images.length;
        document.getElementById("modalImage").src = images[currentIndex];
    }
}

/* ==== LIST/GRID SAHIFA FUNKSIYALARI ==== */
function toggleView() {
    let viewInput = document.getElementById("view-input");
    let form = document.getElementById("filter-form");

    if (viewInput && form) {
        let currentView = viewInput.value;

        if (currentView === "grid") {
            viewInput.value = "list";
        } else {
            viewInput.value = "grid";
        }

        form.submit();
    }
}
