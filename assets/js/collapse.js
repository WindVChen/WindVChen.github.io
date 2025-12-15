$(".header").click(function () {

    $header = $(this);
    //getting the next element
    $content = $header.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $content.slideToggle(500, function () {
        //execute this after slideToggle is done
        //change text of header based on visibility of content div
        if ($content.is(":visible")) {
            $header.html("[ Collapse ]");
            $header.addClass("expanded");
        } else {
            $header.html("[ Show more news ]");
            $header.removeClass("expanded");
        }
        // Ensure cursor style is maintained
        $header.css("cursor", "pointer");
    });

});
