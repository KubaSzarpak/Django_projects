from MySQLdb.times import DateTimeType
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Trip, Country, Client, CountryTrip, ClientTrip


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class SimpleTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['name', 'date_from']


class SimpleClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['firstname', 'lastname']


class AddClientTripSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    telephone = serializers.CharField(max_length=255)
    pesel = serializers.CharField(max_length=255)
    trip_id = serializers.IntegerField()
    trip_name = serializers.CharField(max_length=255)

    class Meta:
        model = ClientTrip
        fields = ['firstname', 'lastname', 'email', 'telephone', 'pesel', 'trip_id', 'trip_name', 'payment_date']

    def validate_client(self) -> int:
        pesel = self.data['pesel']
        if Client.objects.filter(pesel=pesel).exists():
            client_id = Client.objects.values('id').get(pesel=pesel)['id']

            if ClientTrip.objects.filter(client_id=client_id).exists():
                raise ValidationError('Client is already signed to this trip')
        else:
            Client.objects.create(firstname=self.data['firstname'],
                                  lastname=self.data['lastname'],
                                  email=self.data['email'],
                                  telephone=self.data['telephone'],
                                  pesel=pesel)
            client_id = Client.objects.values('id').get(pesel=pesel)['id']
        return client_id

    def validate_trip(self) -> int:
        trip_id = self.data['trip_id']
        trip_name = self.data['trip_name']
        if not Trip.objects.filter(id=trip_id, name=trip_name).exists():
            raise ValidationError('Trip does not exists')

        return trip_id

    def save(self, **kwargs):
        client_id = self.validate_client()
        trip_id = self.validate_trip()
        payment_date = self.data.get('payment_date')

        ClientTrip.objects.create(client_id=client_id,
                                  trip_id=trip_id,
                                  registered_at=DateTimeType.now(),
                                  payment_date=payment_date)
        return self.instance


class CountryTripSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = CountryTrip
        fields = ['country']


class TripClientSerializer(serializers.ModelSerializer):
    client = SimpleClientSerializer()

    class Meta:
        model = ClientTrip
        fields = ['client']


class TripSerializer(serializers.ModelSerializer):
    countries = CountryTripSerializer(many=True)
    clients = TripClientSerializer(many=True)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'description', 'date_from', 'date_to', 'max_people', 'countries', 'clients']
