function goFullscreen() {
    const el = document.getElementById("controller");
    if (el.requestFullscreen) {
        el.requestFullscreen();
    } else if (el.webkitRequestFullscreen) { // Safari
        el.webkitRequestFullscreen();
    } else if (el.msRequestFullscreen) { // IE11
        el.msRequestFullscreen();
    }
}

function goReload() {
    location.reload();
}
