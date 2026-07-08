package com.example.api_gateway;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import reactor.core.publisher.Mono;
import org.springframework.cloud.gateway.filter.ratelimit.RedisRateLimiter; 

@Configuration
public class GatewayConfig {

    //@Value("${SPB_APP_URI:http://spb-app:8081}")
    //private String spbAppUri;

    @Bean
    public RouteLocator customRouteLocator(RouteLocatorBuilder builder, 
                                        RedisRateLimiter redisRateLimiter) {
        //String spbAppUri = env.getProperty("SPB_APP_URI", "http://spb-app:8081");

        return builder.routes()
            .route("spb-app", r -> r.path("/spb/**")
                .filters(f -> f
                    .stripPrefix(1)
                    .requestRateLimiter(config -> {
                        config.setRateLimiter(redisRateLimiter);
                        config.setKeyResolver(exchange -> 
                            Mono.just(exchange.getRequest().getRemoteAddress().getAddress().getHostAddress()));
                    })
                    .circuitBreaker(cfg -> cfg.setName("spbCircuitBreaker")))
                .uri("http://spb-app:8081"))
            .build();
}
}