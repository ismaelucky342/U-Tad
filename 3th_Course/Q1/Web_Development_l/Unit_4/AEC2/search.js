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


// Manejo dela la búsqueda de perros por raza y sub raza

$(document).ready(function() {
    const API_BASE_URL = 'https://dog.ceo/api';
    let allBreeds = {};
    let loadedImages = new Set();

    // Muestro un mensaje de error en la UI
    function showError(message) {
        const errorDiv = $('#error-message');
        const successDiv = $('#success-message');
        
        successDiv.hide();
        errorDiv.text(message);
        errorDiv.fadeIn();
        
        setTimeout(() => {
            errorDiv.fadeOut();
        }, 5000);
    }

    // Muestra un mensaje de éxito en la UI
    function showSuccess(message) {
        const errorDiv = $('#error-message');
        const successDiv = $('#success-message');
        
        errorDiv.hide();
        successDiv.text(message);
        successDiv.fadeIn();
        
        setTimeout(() => {
            successDiv.fadeOut();
        }, 3000);
    }

    // Carga todas las razas desde la API
    function loadBreeds() {
        const breedSelect = $('#breed-select');
        breedSelect.html('<option value="">Cargando razas...</option>');
        breedSelect.prop('disabled', true);

        $.ajax({
            url: `${API_BASE_URL}/breeds/list/all`,
            method: 'GET',
            dataType: 'json',
            success: function(response) {
                if (response.status === 'success' && response.message) {
                    allBreeds = response.message;
                    populateBreedSelect();
                } else {
                    showError('Error al cargar las razas de perros');
                }
            },
            error: function(xhr, status, error) {
                console.error('Error al cargar razas:', error);
                showError('No se pudieron cargar las razas. Verifica tu conexión a internet.');
                breedSelect.html('<option value="">Error al cargar razas</option>');
            }
        });
    }

    // Puebla el dropdown de razas
    function populateBreedSelect() {
        const breedSelect = $('#breed-select');
        breedSelect.empty();
        breedSelect.append('<option value="">Selecciona una raza</option>');

        const sortedBreeds = Object.keys(allBreeds).sort();
        
        sortedBreeds.forEach(breed => {
            const option = $('<option>', {
                value: breed,
                text: capitalize(breed)
            });
            breedSelect.append(option);
        });

        breedSelect.prop('disabled', false);
    }

    // Capitaliza la primera letra de un string
    function capitalize(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    // Maneja el cambio de raza seleccionada
    $('#breed-select').on('change', function() {
        const selectedBreed = $(this).val();
        const subbreedSelect = $('#subbreed-select');

        if (!selectedBreed) {
            subbreedSelect.html('<option value="">Selecciona primero una raza</option>');
            subbreedSelect.prop('disabled', true);
            return;
        }

        const subbreeds = allBreeds[selectedBreed];

        if (subbreeds && subbreeds.length > 0) {
            subbreedSelect.empty();
            subbreedSelect.append('<option value="">Todas las sub-razas</option>');
            
            subbreeds.forEach(subbreed => {
                const option = $('<option>', {
                    value: subbreed,
                    text: capitalize(subbreed)
                });
                subbreedSelect.append(option);
            });
            
            subbreedSelect.prop('disabled', false);
        } else {
            subbreedSelect.html('<option value="">Esta raza no tiene sub-razas</option>');
            subbreedSelect.prop('disabled', true);
        }
    });

    // Maneja el envío del formulario
    $('#search-form').on('submit', function(e) {
        e.preventDefault();

        const breed = $('#breed-select').val();
        const subbreed = $('#subbreed-select').val();
        const count = parseInt($('#image-count').val());

        if (!breed) {
            showError('Por favor, selecciona una raza de perro');
            return;
        }

        if (!count || count < 1 || count > 50) {
            showError('Por favor, introduce una cantidad válida (entre 1 y 50)');
            return;
        }

        loadedImages.clear();
        searchDogImages(breed, subbreed, count);
    });

    // Busca imágenes de perros según los criterios
    function searchDogImages(breed, subbreed, count) {
        const gallery = $('#search-gallery');
        const resultsTitle = $('#results-title');
        const submitButton = $('.btn-search');
        
        gallery.html('<div class="loading">Buscando imágenes...</div>');
        resultsTitle.show();
        submitButton.prop('disabled', true);

        let url;
        if (subbreed) {
            url = `${API_BASE_URL}/breed/${breed}/${subbreed}/images`;
        } else {
            url = `${API_BASE_URL}/breed/${breed}/images`;
        }

        $.ajax({
            url: url,
            method: 'GET',
            dataType: 'json',
            success: function(response) {
                submitButton.prop('disabled', false);
                
                if (response.status === 'success' && response.message) {
                    const images = response.message;
                    
                    if (images.length === 0) {
                        showError('No se encontraron imágenes para esta raza');
                        gallery.empty();
                        return;
                    }

                    const selectedImages = selectImages(images, count);
                    displaySearchResults(selectedImages);
                    
                    const breedName = capitalize(breed) + (subbreed ? ' - ' + capitalize(subbreed) : '');
                    showSuccess(`Se encontraron ${selectedImages.length} imágenes de ${breedName}`);
                } else {
                    showError('Error al obtener las imágenes');
                    gallery.empty();
                }
            },
            error: function(xhr, status, error) {
                submitButton.prop('disabled', false);
                console.error('Error en la búsqueda:', error);
                
                if (xhr.status === 404) {
                    showError('No se encontró la raza o sub-raza especificada');
                } else {
                    showError('Error al buscar imágenes. Por favor, intenta de nuevo.');
                }
                
                gallery.empty();
            }
        });
    }

    // Selecciona imágenes evitando duplicados cuando sea posible
    function selectImages(allImages, count) {
        const availableImages = allImages.length;
        
        if (count > availableImages) {
            showError(`Solo hay ${availableImages} imágenes disponibles para esta raza. Se mostrarán todas.`);
            return allImages;
        }

        const shuffled = [...allImages].sort(() => 0.5 - Math.random());
        return shuffled.slice(0, count);
    }

    // Muestra los resultados de la búsqueda
    function displaySearchResults(imageUrls) {
        const gallery = $('#search-gallery');
        gallery.empty();

        if (!imageUrls || imageUrls.length === 0) {
            gallery.html('<p style="text-align: center; color: var(--text-light);">No se encontraron imágenes</p>');
            return;
        }

        imageUrls.forEach((url) => {
            loadedImages.add(url);
            
            const imageWrapper = $('<div>', {
                class: 'dog-image-wrapper'
            });

            const img = $('<img>', {
                class: 'dog-image',
                src: url,
                alt: 'Imagen de perro',
                loading: 'lazy'
            });

            img.on('error', function() {
                $(this).parent().remove();
                showError('Algunas imágenes no pudieron cargarse');
            });

            imageWrapper.append(img);
            gallery.append(imageWrapper);
        });

        $('html, body').animate({
            scrollTop: $('#results-container').offset().top - 100
        }, 500);
    }

    loadBreeds();
});
