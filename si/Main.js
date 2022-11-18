var myLatLng = { lat: -32.9, lng: -68.8 };
var mapOptions = {
    center: myLatLng,
    zoom: 12,
    mapTypeId: google.maps.MapTypeId.ROADMAP

};

var map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

var directionsService = new google.maps.DirectionsService();

var directionsDisplay = new google.maps.DirectionsRenderer();

directionsDisplay.setMap(map);

function calcRoute() {

    var request = {
        origin: document.getElementById("Desde").value,
        destination: document.getElementById("Hasta").value,
        travelMode: google.maps.TravelMode.DRIVING, 
        unitSystem: google.maps.UnitSystem.IMPERIAL
    }

    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {

            const output = document.querySelector('#output');
            output.innerHTML = "<div class='alert-info'>Desde: " + document.getElementById("Desde").value + ".<br />Hasta: " + document.getElementById("Hasta").value + ".<br /> Distancia de manejo <i class='fas fa-road'></i> : " + result.routes[0].legs[0].distance.text + ".<br />Duracion <i class='fas fa-hourglass-start'></i> : " + result.routes[0].legs[0].duration.text + ".</div>";

            directionsDisplay.setDirections(result);
        } else {

            directionsDisplay.setDirections({ routes: [] });

            map.setCenter(myLatLng);

            output.innerHTML = "<div class='alert-danger'><i class='fas fa-exclamation-triangle'></i> No se pudo calcular la distancia del viaje</div>";
        }
    });

}


var options = {
    types: ['(cities)']
}

var input1 = document.getElementById("Desde");
var autocomplete1 = new google.maps.places.Autocomplete(input1, options);

var input2 = document.getElementById("Hasta");
var autocomplete2 = new google.maps.places.Autocomplete(input2, options);
