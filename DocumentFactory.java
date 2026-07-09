package com.dp.di;

public class CustomerService {
    private final CustomerRepository customerRepository;

    public CustomerService(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public String getCustomerName(String id) {
        return customerRepository.findCustomerById(id);
    }
}
