
const nonallowed_characters = ["<", ">", "$", "/", "\\"];

$( document ).ready(function() {
	$('form').on('submit', function(event) {
		event.preventDefault();
		/**
		replaces the submit button by the spinner button border
		and disable the input field
		*/
		$('#spinerBorderButton').removeClass('d-none');
		$('#submitButton').addClass('d-none');
		$('input').attr("readonly", true);
		/**
		check if user message does not contain any forbidden characters
		*/
		var userMessage = $('#newUserMessage').val();
		for(var i= 0; i < nonallowed_characters.length; i++){
			if (userMessage.includes(nonallowed_characters[i])){
				userMessage = 'nonallowed_characters'
			}
		}
		/**
		sends the message to the back-end
		*/
		$.ajax({
			url : '/newUserMessage',
      type : 'POST',
			dataType: 'json',
			data : { newUserMessage: userMessage	}
		})
		/**
		get back-end datas
		*/
		.done(function(data) {
			if (data){
				/**
				add the user's message to the message zone
				*/
				$('#messagesZone').append(
					/**
					add the user's message to the message zone
					*/
					"<div class='row'>"
					+ "<div class='d-none d-sm-block col-md-2 mt-1 py-1'></div>"
					+ "<div class='userMessage rounded bg-info col-md-9 mt-1 py-1'>"
					+ "Vous : "
					+ userMessage
					+ '</div>'
					+ "<div class='d-none d-sm-block col-md-1 mt-1 py-1'></div>"
					+ '</div>'
					);
				/**
				clears the input field
				*/
				$('#newUserMessage').val('');
				/**
				if grandpy add grandpy's answer to the message area
				*/
				if (data.status == 'problem'){
					$('#messagesZone').append(
						"<div class='row'>"
						+ "<div class='d-none d-sm-block col-md-1 mt-1 py-1'></div>"
						+ "<div class='"
						+ "grandpyMessage rounded text-white bg-secondary col-md-9 mt-1 py-1'>"
						+ "GrandPy : "
						+ data.grandpyMessage
						+ '</div>'
						+ "<div class='map'>"
						+ '</div>'
						+ "<div class='d-none d-sm-block col-md-2 mt-1 py-1'></div>"
						+ '</div>'
					);
				}
				else if (data.status == 'ok'){
					$('#messagesZone').append(
						"<div class='row'>"
						+ "<div class='d-none d-sm-block col-md-1 mt-1 py-1'></div>"
						+ "<div class='"
						+ "grandpyMessage rounded text-white bg-secondary col-md-9 mt-1 py-1'>"
						+ "GrandPy : "
						+ data.grandpyMessage.intro_name
						+ data.grandpyMessage.name
						+ data.grandpyMessage.intro_address
						+ data.grandpyMessage.address
						+ data.grandpyMessage.intro_map
						+ '<img src="' + data.grandpyMessage.map_url
						+'" href="' + data.grandpyMessage.map_url
						+'" class="img-fluid py-1">'
						+ data.grandpyMessage.intro_description
						+ data.grandpyMessage.description_first_part
						+'<a id="collapsible">'
						+'<a id="collapseZero" class="collapse">'
						+ data.grandpyMessage.description_collapsible_part
						+'</a>'
						+'<a href="#collapseZero"'
						+' class="btn btn-secondary btn-sm border mb-1"'
						+' data-toggle="collapse" data-parent="#collapsible">+/-</a>'
						+'</a><br>'
						+ '<a href="'
						+ data.grandpyMessage.wikipedia_url
						+'" class="btn btn-light btn-sm mb-2" role="button"'
					  + 'target="_blank">En savoir plus sur Wikipedia</a>'
						+ '</div>'
						+ "<div class='map'>"
						+ '</div>'
						+ "<div class='d-none d-sm-block col-md-2 mt-1 py-1'></div>"
						+ '</div>'
					);
				}
				/**
				scroll down the message area
				replaces the spiner border button with the submit button
				activate the input field
				*/
				$('#messagesZone').scrollTop( 10000 );
				$('#spinerBorderButton').addClass('d-none');
				$('#submitButton').removeClass('d-none');
				$('input').attr("readonly", false);
			}
		});
	});
});
