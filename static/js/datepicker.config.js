$(document).ready(function() {

  var locale = {
    "format": "YYYY/MM/DD",
    "separator": " - ",
    "applyLabel": "Aceptar",
    "cancelLabel": "Cancelar",
    "fromLabel": "Desde",
    "toLabel": "A",
    "customRangeLabel": "Custom",
    "daysOfWeek": [
        "Dom",
        "Lun",
        "Mar",
        "Mie",
        "Jue",
        "Vie",
        "Sab"
    ],
    "monthNames": [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agusto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ],
    "firstDay": 1
  }

  // Configuracion del datepicker

  $(function() {
    $('input[name="fechas"]').daterangepicker({
      opens: 'right',
      minDate: moment(),
      "buttonClasses": "btn",
      "applyButtonClasses": "btn-info",
      "cancelClass": "btn-danger",
      "locale": locale
    });

    $('input[name="fecha_nacimiento"]').daterangepicker({
      "locale": locale,
      singleDatePicker: true,
      showDropdowns: true,
      minYear: 1901,
      maxYear: (parseInt(moment().format('YYYY'),10) - 18),
      maxDate: moment().subtract(18, 'year'),
    }, function(start, end, label) {
      var years = moment().diff(start, 'years');
      if(years<18){
        alert("Debes ser mayor de edad para usar nuestros servicios ");
      }
    });
  });
});
