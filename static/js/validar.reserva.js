$(document).ready(function() {
  $('#nombre, #ci, #email, #tel, #ap_pat, form').on('keyup focus change', function() {
		if(
      $('#nombre').data('valid')=='true'
      && $('#email').data('valid')=='true'
      && $('#tel').data('valid')=='true'
      && $('#ap_pat').data('valid')=='true'
      && $('#ci').data('valid')=='true'
    )
    {
			$('#enviar').removeClass('btn-danger');
			$('#enviar').addClass('btn-success');
			$('#enviar').removeAttr('disabled');
		}else{
			$('#enviar').removeClass('btn-success');
			$('#enviar').addClass('btn-danger');
			$('#enviar').attr('disabled', 'disabled');
		}
	});

  $('#ci').on('keyup focus', function () {
		var ci = $(this).val();
		if(ci.length > 8){
			$('#ci').data('valid', 'true');
			$(this).removeClass('is-invalid');
			$(this).addClass('is-valid');
			$('#ci_feed').removeClass('invalid-feedback');
			$('#ci_feed').addClass('valid-feedback');
			$('#ci_feed').html('Correcto');
		}else{
			$('#ci').data('valid', 'false');
			$(this).removeClass('is-valid');
			$(this).addClass('is-invalid');
			if(ci.length <= 0){
				$('#ci_feed').addClass('invalid-feedback');
				$('#ci_feed').html('Debe ingresar un DNI / Pasaporte');
			}else{
				$('#ci_feed').addClass('invalid-feedback');
				$('#ci_feed').html('El DNI debe ser mayor a 9 carateres');
			}
		}
	});

	$('#nombre').on('keyup focus', function () {
		var nombre = $(this).val();
		if(nombre.length > 3){
			$('#nombre').data('valid', 'true');
			$(this).removeClass('is-invalid');
			$(this).addClass('is-valid');
			$('#nombre_feed').removeClass('invalid-feedback');
			$('#nombre_feed').addClass('valid-feedback');
			$('#nombre_feed').html('Correcto');
		}else{
			$('#nombre').data('valid', 'false');
			$(this).removeClass('is-valid');
			$(this).addClass('is-invalid');
			if(nombre.length <= 0){
				$('#nombre_feed').addClass('invalid-feedback');
				$('#nombre_feed').html('Debe ingresar un nombre');
			}else{
				$('#nombre_feed').addClass('invalid-feedback');
				$('#nombre_feed').html('El nombre debe ser mayor a 3 carateres');
			}
		}
	});

  $('#ap_pat').on('keyup focus', function () {
		var ap_pat = $(this).val();
		if(ap_pat.length > 3){
			$('#ap_pat').data('valid', 'true');
			$(this).removeClass('is-invalid');
			$(this).addClass('is-valid');
			$('#ap_pat_feed').removeClass('invalid-feedback');
			$('#ap_pat_feed').addClass('valid-feedback');
			$('#ap_pat_feed').html('Correcto');
		}else{
			$('#ap_pat').data('valid', 'false');
			$(this).removeClass('is-valid');
			$(this).addClass('is-invalid');
			if(ap_pat.length <= 0){
				$('#ap_pat_feed').addClass('invalid-feedback');
				$('#ap_pat_feed').html('Debe ingresar el primer apellido');
			}else{
				$('#ap_pat_feed').addClass('invalid-feedback');
				$('#ap_pat_feed').html('El apellido debe ser mayor a 3 carateres');
			}
		}
	});

	$('#email').on('keyup focus', function () {
		var email = $(this).val();
		var reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
		if(reg.exec(email)){
			$('#email').data('valid', 'true');
			$(this).removeClass('is-invalid');
			$(this).addClass('is-valid');
			$('#email_feed').removeClass('invalid-feedback');
			$('#email_feed').addClass('valid-feedback');
			$('#email_feed').html('Correcto');
		}else{
			$('#email').data('valid', 'false');
			$(this).removeClass('is-valid');
			$(this).addClass('is-invalid');
			if(email.length <= 0){
				$('#email_feed').addClass('invalid-feedback');
				$('#email_feed').html('Debe ingresar un email');
			}else{
				$('#email_feed').addClass('invalid-feedback');
				$('#email_feed').html('El email debe cumplir con formato');
			}
		}
	});

	$('#tel').on('keyup focus', function () {
		var tel = $(this).val();
		if(tel.length==9){
			$('#tel').data('valid', 'true');
			$(this).removeClass('is-invalid');
			$(this).addClass('is-valid');
			$('#tel_feed').removeClass('invalid-feedback');
			$('#tel_feed').addClass('valid-feedback');
			$('#tel_feed').html('Correcto');
		}else{
			$('#tel').data('valid', 'false');
			$(this).removeClass('is-valid');
			$(this).addClass('is-invalid');
			if(tel===''){
				$('#tel_feed').addClass('invalid-feedback');
				$('#tel_feed').html('Debe ingresar un telefono');
			}else{
				$('#tel_feed').addClass('invalid-feedback');
				$('#tel_feed').html('El telefono debe tener 9 digitos');
			}
		}
	});

});
