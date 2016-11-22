/* Copyright 2016 LasLabs Inc.
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl). */

odoo.define("pharmacy.tour", function (require) {
    "use strict";
    
    var core = require('web.core');
    var tour = require('web_tour.tour');
    
    var _t = core._t;
    
    tour.STEPS.PHARMACY = [
        tour.STEPS.MENU_MORE,
        {
            trigger: '.o_app[data-menu-xmlid="medical_app_pharmacy.pharmacy_app_menu"], ' +
                     '.oe_menu_toggler[data-menu-xmlid="medical_app_pharmacy.pharmacy_app_menu"]',
            content: _t('The <b>Pharmacy</b> app allows you to dispense medications in style!'),
            position: 'bottom',
        },
        {
            trigger: '.o_app[data-menu-xmlid="medical_app_pharmacy.dispensing_menu"], ' +
                     '.oe_menu_toggler[data-menu-xmlid="medical_app_pharmacy.dispensing_menu"]',
            content: _t('Use the <b>Dispensing</b> menu to manage prescription orders.'),
            position: 'bottom',
        },
    ];
    
    tour.register('pharmacy_tour', {
        url: "/web",
    },
        tour.STEPS.PHARMACY
    );

});
