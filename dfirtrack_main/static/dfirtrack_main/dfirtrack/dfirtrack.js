// ####################################
// #
// # generic functions
// #
// ####################################

// go to lastpage (used for cancel button)
function lastpage() {
    window.history.back();
}

// close window (used for cancel popup button to close popup window)
function window_close() {
    window.close()
}

// reload parent page if child page is closed (used when save or cancel button is pushed in popup window or if it is closed)
window.onunload = refreshParent;
function refreshParent() {
    window.opener.location.reload();
}

// ####################################
// #
// # popup window related functions
// #
// ####################################

// popup window for adding company
var company_add_popup;
function company_add_popup() {
    company_add_popup = window.open("/company/add_popup/", "company_add_popup", "height=600, width=1000");
}

// popup window for adding contact
var contact_add_popup;
function contact_add_popup() {
    contact_add_popup = window.open("/contact/add_popup/", "contact_add_popup", "height=600, width=1000");
}

// popup window for adding domain
var domain_add_popup;
function domain_add_popup() {
    domain_add_popup = window.open("/domain/add_popup/", "domain_add_popup", "height=600, width=1000");
}

// popup window for adding dnsname
var dnsname_add_popup;
function dnsname_add_popup() {
    dnsname_add_popup = window.open("/dnsname/add_popup/", "dnsname_add_popup", "height=600, width=1000");
}

// popup window for adding location
var location_add_popup;
function location_add_popup() {
    location_add_popup = window.open("/location/add_popup/", "location_add_popup", "height=600, width=1000");
}

// popup window for adding operating system
var os_add_popup;
function os_add_popup() {
    os_add_popup = window.open("/os/add_popup/", "os_add_popup", "height=600, width=1000");
}

// popup window for adding reason
var reason_add_popup;
function reason_add_popup() {
    reason_add_popup = window.open("/reason/add_popup/", "reason_add_popup", "height=600, width=1000");
}

// popup window for adding recommendation
var recommendation_add_popup;
function recommendation_add_popup() {
    recommendation_add_popup = window.open("/recommendation/add_popup/", "recommendation_add_popup", "height=600, width=1000");
}

// popup window for adding serviceprovider
var serviceprovider_add_popup;
function serviceprovider_add_popup() {
    serviceprovider_add_popup = window.open("/serviceprovider/add_popup/", "serviceprovider_add_popup", "height=600, width=1000");
}

// popup window for adding systemtype
var systemtype_add_popup;
function systemtype_add_popup() {
    systemtype_add_popup = window.open("/systemtype/add_popup/", "systemtype_add_popup", "height=600, width=1000");
}

// popup window for system exporter spreadsheet csv system config
var system_exporter_spreadsheet_csv_system_config_popup;
function system_exporter_spreadsheet_csv_system_config_popup() {
    system_exporter_spreadsheet_csv_system_config_popup = window.open("/system/exporter/spreadsheet/csv/system/config/", "system_exporter_spreadsheet_csv_system_config_popup", "height=800, width=600");
}

// ####################################
// #
// # go to top of page button
// #
// ####################################

// go to top of page button (onscroll event)
window.onscroll = function() {show_button()};

// go to top of page button (show btn-top if 20px are scrolled down)
function show_button() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("btn-top").style.display = "block";
    } else {
        document.getElementById("btn-top").style.display = "none";
    }
}

// go to top of page button (on click of button)
function go_to_top() {
    document.body.scrollTop = 0; // Safari
    document.documentElement.scrollTop = 0; // Chrome and Firefox
}
