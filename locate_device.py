from jnius import autoclass

def get_device_location():
    LocationManager = autoclass('android.location.LocationManager')
    Context = autoclass('android.content.Context')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    
    # Get the location manager
    location_manager = PythonActivity.mActivity.getSystemService(Context.LOCATION_SERVICE)
    
    # Check if GPS is enabled
    is_gps_enabled = location_manager.isProviderEnabled(LocationManager.GPS_PROVIDER)
    
    if is_gps_enabled:
        # Get the last known location
        location = location_manager.getLastKnownLocation(LocationManager.GPS_PROVIDER)
        
        if location:
            latitude = location.getLatitude()
            longitude = location.getLongitude()
            return latitude, longitude
        else:
            print("Location information not available.")
    else:
        print("GPS is not enabled.")

if __name__ == "__main__":
    location = get_device_location()
    if location:
        print("Device location (latitude, longitude):", location)
