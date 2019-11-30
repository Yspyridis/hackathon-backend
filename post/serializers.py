from rest_framework import serializers

from .models import Coordinate

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ("name", "x", "y")

    def update(self, instance, validated_data):
        # instance.node_id = validated_data.get("node_id", instance.node_id)
        # instance.node_ip_address = validated_data.get("node_ip_address", instance.node_ip_address)
        # instance.asset_location = validated_data.get("asset_location", instance.asset_location)
        # instance.reputation_value = validated_data.get("reputation_value", instance.reputation_value)
        # instance.reputation_change_speed = validated_data.get("reputation_change_speed", instance.reputation_change_speed)
        # instance.timestamp = validated_data.get("timestamp", instance.timestamp)
        # instance.asset_value = validated_data.get("asset_value", instance.asset_value)
        #
        # instance.save()
        return instance
