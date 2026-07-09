package com.dp.di;

import java.util.Map;

public class CustomerRepositoryImpl implements CustomerRepository {
    private final Map<String, String> customers = Map.of(
        "C001", "John Smith",
        "C002", "Jane Doe"
    );

    @Override
    public String findCustomerById(String id) {
        return customers.getOrDefault(id, "Customer not found");
    }
}
