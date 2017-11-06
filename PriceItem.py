class PriceItem(object):
    def __init__(self, name, unit, quantity, price, currency, place, date):
        self.name=name
        self.unit=unit
        self.quantity=float(quantity)
        self.price=float(price)
        self.currency=currency
        self.place=place
        self.date=date

    def to_document(self):
        return dict(
            name=self.name,
            unit=self.unit,
            quantity=self.quantity,
            price=self.price,
            currency=self.currency,
            place=self.place,
            date=self.date
        )

    @classmethod
    def from_document(cls, doc):
        return cls(
            name=doc['name'],
            unit=doc['unit'],
            quantity=doc['quantity'],
            price=doc['price'],
            currency=doc['currency'],
            place=doc['place'],
            date=doc['date']
        )
