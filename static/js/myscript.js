function initMap() {
  let options = {
    center: { lat: 30.3753, lng: 69.3451 },
    zoom: 8
  }
  map = new google.maps.Map(document.getElementById("map"), options);

  google.maps.event.addListener(map, 'click', function (event) {
    placeMarker(map, event.latLng);
  });

  let marker;

  function placeMarker(map, location) {
    if (marker) {
      marker.setMap(null);
    }
    marker = new google.maps.Marker({
      position: location,
      map: map
    });
    var infowindow = new google.maps.InfoWindow({
      content: 'Latitude: ' + location.lat() +
        '<br>Longitude: ' + location.lng()
    });
    document.querySelector("#longitude").value = location.lng();
    document.querySelector("#latitude").value = location.lat();
    infowindow.open(map, marker);
  }
  //https://youtu.be/bUYYaJoXw9c(to connect form)

  $(document).ready(function () {
    let MapDiv = $(".map");
    let Form = $("#test");
    let MapButton = $(".mapButton");
    let cordbutton = $(".cordButton");
    MapButton.click(function () {
      Form.css("display", "none");
      MapDiv.css("display", "inline-block");
    });
    cordbutton.click(function () {
      MapDiv.css("display", "none");
      Form.css("display", "inline-block");
    });
  });
}