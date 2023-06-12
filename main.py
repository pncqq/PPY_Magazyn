from warehouse_managment_system import WarehouseManagementSystem

warehouse = WarehouseManagementSystem()

warehouse.connect_to_database()
warehouse.run()
warehouse.disconnect_from_database()

# TODO:
# 1. Wyszukiwanie produktów DONE
# 2. Usuwanie produktów DONE

# 3. Sortowanie wyników wyszkuwania
# 4. Filtrowanie raportów wg. kryteriów
