import json
import traceback
from http import HTTPStatus
from datetime import datetime

class WidgetException(Exception):
    message = "A server error occcured"
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args, customer_message=None):
        super().__init__(*args)
        if args:
            self.message = args[0]
        self.customer_message = customer_message if customer_message is not None else self.message

    def to_json(self):
        response = {
                "code": self.http_status.value,
                "message": f"{self.http_status.phrase}: {self.customer_message}",
                "category": type(self).__name__,
                "time_utc": datetime.utcnow().isoformat()
               }
        return json.dumps(response)

    @property
    def traceback(self):
        return traceback.format_exc()

    def log_exception(self):
        exception = {
            "type": self.__class__.__name__,
            "code": self.http_status.value,
            "message": f"{self.message}",
            "args": self.args[1:],
            "traceback": self.traceback
        }
        print(f"EXCEPTION: {datetime.utcnow().isoformat()}: {exception}")

class SupplierException(WidgetException):
    message = "A supplier exception happened"

class NotManufacturedAnymore(SupplierException):
    message = "Widget is not manufactured anymore"

class ProductionDelayed(SupplierException):
    message = "Widget production delayed"

class ShippingDelayed(SupplierException):
    message = "Widget shipping delayed"

class CheckoutException(WidgetException):
    message = "Exception at the checkout"

class InventoryTypeException(CheckoutException):
    message = "Inventory exception happend"

class OutOfStockException(InventoryTypeException):
    message = "Widget components are out of stock"

class PricingException(CheckoutException):
    message = "A pricing exception happened"

class InvalidCouponCode(PricingException):
    message = "There is an invalid coupon code exception"
    http_status = HTTPStatus.BAD_REQUEST

class CannotStackCoupons(PricingException):
    message = "Cannot stack coupons"
    http_status = HTTPStatus.BAD_REQUEST

if __name__ == '__main__':
    try:
        raise InvalidCouponCode("There is an issue with the coupon code")
    except WidgetException as ex:
        ex.log_exception()
        print(ex.to_json())
