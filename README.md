# Prasarana GTFS-Realtime Parser

A Python-based utility to fetch, decode, and convert Malaysia's **Prasarana (RapidKL)** vehicle position data from Protocol Buffer (`.proto`) format to human-readable JSON.

## Overview

This project interacts with the **Official Open API of Malaysia (data.gov.my)**. It specifically targets the GTFS-Realtime feed for Prasarana, which provides live updates on vehicle positions across the RapidKL bus and rail network.

### Data Source
- **API Endpoint:** `https://api.data.gov.my/gtfs-realtime/vehicle-position/prasarana`
- **Agency:** Prasarana Malaysia Berhad
- **Format:** Protocol Buffers (.proto)
- **Update Frequency:** Every 30 seconds

## Documentation
URL: `https://developer.data.gov.my/realtime-api/gtfs-realtime`

## Features
- Fetches live binary `.proto` data from the Malaysian Government's Open API.
- Deserializes GTFS-Realtime messages using official Google transit bindings.
- Exports real-time vehicle coordinates, trip IDs, and license plate labels to JSON.
- Supports multiple categories: `rapid-bus-kl`, `rapid-bus-mrtfeeder`, `rapid-bus-kuantan`, and `rapid-bus-penang`.

## Installation

You will need the official Google Protocol Buffer bindings for GTFS and the `requests` library:

```bash
pip install gtfs-realtime-bindings protobuf requests

