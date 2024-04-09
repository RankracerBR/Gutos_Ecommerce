function toggleUrls(moduleId) {
    var urls = document.getElementById(moduleId);
    if (urls.style.display === 'none') {
        urls.style.display = 'block';
    } else {
        urls.style.display = 'none';
    }
}

document.getElementById('acesso').addEventListener('click', function() {
    toggleUrls('urls-acesso');
});

document.getElementById('usuarios').addEventListener('click', function() {
    toggleUrls('urls-usuarios');
});

document.getElementById('produtos').addEventListener('click', function() {
    toggleUrls('urls-produtos');
});