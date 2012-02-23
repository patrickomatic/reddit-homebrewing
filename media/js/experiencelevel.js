$(document).ready(function() {
	$("#experience-level-picker a").click(function() {
		$.post('/experience/level', {
				'experience_level': $(this).attr("data-value"),
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
			}, function (data, textStatus) {
				alert("data = " + data);
				alert("textStatus = " + textStatus);
		});
	});
});
