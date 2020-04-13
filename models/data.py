import xml.etree.ElementTree as ET
from lib import Errors


class TrackingData(object):
    MINIMUM_NUMBER_SPOTS_ALLOWED = 20

    def __init__(self):
        self._all_tracks = None
        self._all_spots = None
        self._visualisation_data = None
        self.version = None

    @staticmethod
    def from_xml_root(root):
        tracking_data = TrackingData()
        tracking_data.update_from_xml_root(root)
        return tracking_data

    def update_from_xml_root(self, root):
        try:
            self._update_from_xml_root(root)
        except ET.ParseError:
            raise Errors.XML_FILE_INVALID

    def _update_from_xml_root(self, root):
        if 'TrackMate' != root.tag:
            raise Errors.XML_FILE_INVALID

        self.version = root.attrib.get('version')

        element_all_spots = root.find('Model/AllSpots')
        self._all_spots = {}
        for e_frame in element_all_spots:
            for e_spot in e_frame:
                self._all_spots[e_spot.attrib.get('ID')] = e_spot.attrib

        element_all_tracks = root.find('Model/AllTracks')
        self._all_tracks = {}
        for e_track in element_all_tracks:
            nb_spot_in_track = int(e_track.attrib.get('NUMBER_SPOTS'))
            if nb_spot_in_track < TrackingData.MINIMUM_NUMBER_SPOTS_ALLOWED:
                continue
            track_name = e_track.attrib.get('name')
            track_attrib = e_track.attrib
            edges = []
            for e_edge in e_track:
                edges.append(e_edge.attrib)
            self._all_tracks[track_name] = {'attrib': track_attrib, 'edges': edges}

    def visualisation_data(self):
        # currently only for plotly
        if self._visualisation_data is None:
            self._visualisation_data = self._generate_visualisation_data()

        return self._visualisation_data

    def _generate_visualisation_data(self):
        visualisation_data = {}
        for track_name, track in self._all_tracks.items():
            dict_spots = {}
            # put all spots together, we don't want to split the track to branches
            for edge in track['edges']:
                spot_source_id = edge.get('SPOT_SOURCE_ID')
                spot_source = self._all_spots.get(spot_source_id)
                if spot_source is None:
                    continue
                dict_spots[spot_source_id] = TrackingData._get_x_y_t_from_spot(spot_source)

                spot_target_id = edge.get('SPOT_TARGET_ID')
                spot_target = self._all_spots.get(spot_target_id)
                if spot_target is None:
                    continue
                dict_spots[spot_target_id] = TrackingData._get_x_y_t_from_spot(spot_target)

            visualisation_coordinates = TrackingData._dict_spots_to_visualisation_coordinates(dict_spots)
            visualisation_data[track_name] = {'attrib': track['attrib'], 'spots': visualisation_coordinates}

        return visualisation_data

    @staticmethod
    def _get_x_y_t_from_spot(spot):
        return [int(float(spot['POSITION_X'])), int(float(spot['POSITION_Y'])), int(spot['FRAME'])]

    @staticmethod
    def _dict_spots_to_visualisation_coordinates(spots):
        spots_coordinates_x = []
        spots_coordinates_y = []
        spots_coordinates_t = []
        for v in spots.values():
            spots_coordinates_x.append(v[0])
            spots_coordinates_y.append(v[1])
            spots_coordinates_t.append(v[2])
        return {'x': spots_coordinates_x, 'y': spots_coordinates_y, 'z': spots_coordinates_t}

    def __str__(self):
        return 'all_tracks: {}\nall_spots: {}\nversion: {}'.format(
            self._all_tracks,
            self._all_spots,
            self.version
        )

    def to_sql(self):
        # TODO: to table
        pass


class DataContainerType:
    MYSQL = 1


class DataContainer(object):
    """A base class to store tracking data"""
    def __init__(self):
        self.data = None
        self.id = None
        self.title = None
        self.comment = None
        self.type = None
        self.version = None

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'comment': self.comment,
            'content': self.data.visualisation_data()
        }

    def __str__(self):
        return 'data: {}'.format(self.data)
