import contextlib
import io
import json
from pathlib import Path
import unittest

notebook = json.loads((Path(__file__).parents[1] / "Hotel_Management.ipynb").read_text(encoding="utf-8"))
scope = {"__name__": "hotel_tests"}
for cell in notebook["cells"]:
    if cell["cell_type"] == "code":
        exec("".join(cell["source"]), scope)


class HotelTests(unittest.TestCase):
    def test_sorting_does_not_change_booking_order(self):
        hotels = []
        for name, rating in [("Zulu", 2), ("Alpha", 5), ("Middle", 3)]:
            hotel = scope["Hotel"]()
            hotel.name, hotel.rating = name, rating
            hotels.append(hotel)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            scope["SortHotelByName"](hotels)
        self.assertLess(output.getvalue().index("HotelName:Alpha"), output.getvalue().index("HotelName:Zulu"))
        self.assertEqual([hotel.name for hotel in hotels], ["Zulu", "Alpha", "Middle"])
        scope["Hotel"].sortByRate()
        self.assertEqual([hotel.rating for hotel in sorted(hotels)], [2, 3, 5])

    def test_variable_record_count_and_length_validation(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            scope["HotelManagement"](["User"], [1], ["Only Hotel"], [50], [2], ["City"], [4], [50])
        self.assertIn("Hotel name: Only Hotel", output.getvalue())
        with self.assertRaises(ValueError):
            scope["HotelManagement"](["User"], [], ["Hotel"], [50], [2], ["City"], [4], [50])


if __name__ == "__main__":
    unittest.main()
