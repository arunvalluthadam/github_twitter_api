// ------------------------------ Twitter Ajax -----------------------------------------

$(function() {
	$('#twitter_ajax').keyup(function() {
		$.ajax({
			type: "POST",
			url: "/twitter-ajax/",
			data: {
				'twitter_text': $('#twitter_ajax').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
			},
			success: twitterSuccess,
			dataType: 'html'
		});
	});
});

function twitterSuccess(data, textStatus, jqXHR)
{
	$('#tweet-results').html(data);
}


// -------------------------------- Github Ajax ----------------------------------------

$(function() {
	$('#github_ajax').keyup(function() {
		$.ajax({
			type: "POST",
			url: "/github-ajax/",
			data: {
				'github_text': $('#github_ajax').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
			},
			success: githubSuccess,
			dataType: 'html'
		});
	});
});

function githubSuccess(data, textStatus, jqXHR)
{
	$('#github-results').html(data);
}