"""Utilities for parsing CRS"""
import os
import contextlib
from pathlib import Path

import pyproj


def get_geodetic_crs(crs):
    """Returns name of Geodetic CRS"""
    return crs.source_crs.to_json_dict()["name"]


def get_datum_name(crs):
    """Returns name of datum"""
    try:
        datum_name = crs.geodetic_crs.to_json_dict()["datum"]["name"]
    except KeyError as err:
        datum_name = "Unknown"
    return datum_name


def get_epsg_version_string():
    """Returns version and revision date of EPSG Database"""
    return (f"{pyproj.database.get_database_metadata('EPSG.VERSION')},  "
            f"{pyproj.database.get_database_metadata('EPSG.DATE')}")


def get_coordinate_operation(crs):
    """Returns name of projection"""
    return crs.coordinate_operation.to_json_dict()["name"]


def get_coordinate_system(crs):
    """Returns coordinate system name"""
    dims = len(crs.coordinate_system.to_json_dict()["axis"])
    return f"{dims}D {crs.coordinate_system.to_json_dict()['subtype']}"


def dd2dms(dd):
    """Converts decimal degrees to degree minutes seconds.  seconds are decimal"""
    return


@contextlib.contextmanager
def working_directory(path):
    """Changes working directory and returns to previous on exit."""
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)
