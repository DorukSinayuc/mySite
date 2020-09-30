$('.js--scroll-to-experiments').click(function () {
  $('html, body').animate({scrollTop: $('.blog__content--containerExperiments').offset().top}, 1000);
});

$('.js--scroll-to-intTopics').click(function () {
  $('html, body').animate({scrollTop: $('.blog__content--containerInterestingTopics').offset().top}, 1000);
});

$('.js--scroll-to-notes').click(function () {
  $('html, body').animate({scrollTop: $('.blog__content--containerNotes').offset().top}, 1000);
});
