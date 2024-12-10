from pages.cart_page import Cart_page
from pages.proteins_page import Proteins_page
from pages.main_page import Main_page
from pages.sport_page import Sport_page
from pages.sportpit_page import Sportpit_page


def test_login(driver):
    mp = Main_page(driver)
    mp.autorization()
    mp.pick_sport_category()

    sp = Sport_page(driver)
    sp.click_sports_nutrition_category_button()

    spp = Sportpit_page(driver)
    spp.click_protein_category_button()

    pp = Proteins_page(driver)
    pp.setting_up_filters()
    pp.add_product_and_move_to_cart()

    cp = Cart_page(driver)
    cp.finish()
