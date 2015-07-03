
var browser = navigator.vendor.toLowerCase();

if (browser == 'apple computer, inc.') {
	document.getElementById('brandLogo').style.maxHeight = "400%";
}

$(document).ready(function() {
	// Tokens available: %y = years, %m = months, %w = weeks, %d = days, %h = hours, %i = minutes, %s = seconds
	
	$("#countdown").countdown({
		date: "September 7, 2015 00:00",
		omitZero: false,
		minsOnly: false,
		leadingZero: true,
		yearsAndMonths: true,
		weeks: true,
		template: "%m %w %d %i %s"
	});
});