// Map with marker

function initMap(){
    // Options for Map
    let options = {
        zoom: 14,
        center: {lat:51.512968, lng:-0.124154}
    }

    // New Map
    let map = new
    google.maps.Map(document.getElementById('map'), options);

    // Add marker
    let marker = new google.maps.Marker({
        position:{lat:51.512658, lng:-0.123987}, 
        map: map
        });
}