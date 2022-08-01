function initMap() {
    // Latitude and Longitude
    var myLatLng = {lat: 6.417523, lng: 7.521754};

    var map = new google.maps.Map(document.getElementById('google-maps'), {
        zoom: 17,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Golden villa Crescent' // Title Location
    });
}