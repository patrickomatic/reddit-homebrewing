$(document).ready(function() {
	$("#experience-level-picker a").click(function() {
		$.ajax({
			'url': '/experience/level',
			'type': 'POST',
			'data': {
				'experience_level': $(this).attr("data-value"),
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
			}, 
			'context': $(this),
			'dataType': 'json',
			'success': function(json) {
				if (json.success) {
					$("#experience-level-picker a").removeClass("selected");
					$(this).addClass('selected');
				} else {
					$("#messages").html("<ul><li class=\"errorlist\">" + json.message + "</li></ul>");
				}
			}
		});

		return false;
	});
});
