from rest_framework import serializers


from applications.ranobe.models import Ranobe


class RanobeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranobe
        fields = '__all__'
