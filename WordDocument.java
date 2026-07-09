package com.dp.di;

public class Main {
    public static void main(String[] args) {
        CustomerRepository repository = new CustomerRepositoryImpl();
        CustomerService service = new CustomerService(repository);

        System.out.println(service.getCustomerName("C001"));
        System.out.println(service.getCustomerName("C999"));
    }
}
