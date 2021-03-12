from marshmallow import Schema, fields


class WeatherSummarySchema(Schema):

    class Meta:
        load_only = (
            "longitude",
            "latitude",
        )

    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
    max = fields.Nested("StatisticsSchema", required=True)
    min = fields.Nested("StatisticsSchema", required=True)
    avg = fields.Nested("StatisticsSchema", required=True)


class StatisticsSchema(Schema):

    temperature = fields.Float(required=True)
    precipitation = fields.Float(required=True)
