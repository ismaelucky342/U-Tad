//====================================================================================================//
//                                                                                                    //
//                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        //
//      AEC2 - PWIC                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       //
//                                                        ██║   ██║█████╗██║   ███████║██║  ██║       //
//      created:        01/12/2025  -  21:45:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       //
//      last change:    05/12/2025  -  00:55:42           ╚██████╔╝      ██║   ██║  ██║██████╔╝       //
//                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        //
//                                                                                                    //
//      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             //
//                                                                                                    //
//      Github:                                           https://github.com/ismaelucky342            //
//                                                                                                    //
//====================================================================================================//

$(document).ready(function() {
    const API_BASE_URL = 'https://dog.ceo/api';
    const IMAGE_COUNT = 5;

    // Muestra un mensaje de error en la UI
    function showError(message) {
        const errorDiv = $('#error-message');
        errorDiv.text(message);
        errorDiv.fadeIn();
        
        setTimeout(() => {
            errorDiv.fadeOut();
        }, 5000);
    }

    // Carga imágenes aleatorias de perros desde la API
    function loadRandomDogs() {
        const gallery = $('#dog-gallery');
        gallery.html('<div class="loading">Cargando imágenes...</div>');

        $.ajax({
            url: `${API_BASE_URL}/breeds/image/random/${IMAGE_COUNT}`,
            method: 'GET',
            dataType: 'json',
            success: function(response) {
                if (response.status === 'success' && response.message) {
                    displayImages(response.message);
                } else {
                    showError('Error al obtener las imágenes de la API');
                }
            },
            error: function(xhr, status, error) {
                console.error('Error en la petición:', error);
                showError('No se pudieron cargar las imágenes. Por favor, verifica tu conexión a internet.');
                gallery.html('');
            }
        });
    }

    // Muestra las imágenes en el contenedor
    function displayImages(imageUrls) {
        const gallery = $('#dog-gallery');
        gallery.empty();

        if (!imageUrls || imageUrls.length === 0) {
            showError('No se encontraron imágenes');
            return;
        }

        imageUrls.forEach((url) => {
            const imageWrapper = $('<div>', {
                class: 'dog-image-wrapper'
            });

            const img = $('<img>', {
                class: 'dog-image',
                src: url,
                alt: 'Imagen de perro aleatorio',
                loading: 'lazy'
            });

            // Manejo de errores al cargar la imagen
            img.on('error', function() {
                $(this).attr('src', 'https://via.placeholder.com/300?text=Error+al+cargar');
            });

            imageWrapper.append(img);
            gallery.append(imageWrapper);
        });
    }

    // Cargar imágenes al iniciar la página
    loadRandomDogs();
});
